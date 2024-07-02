import torch
import torch.nn as nn
import torch.nn.functional as F

from ._base import Distiller

def normalize(logit):
    mean = logit.mean(dim=-1, keepdims=True)
    stdv = logit.std(dim=-1, keepdims=True)
    return (logit - mean) / (1e-7 + stdv)

def kd_loss(logits_student_in, logits_teacher_in, temperature, logit_stand):
    logits_student = normalize(logits_student_in) if logit_stand else logits_student_in
    logits_teacher = normalize(logits_teacher_in) if logit_stand else logits_teacher_in
    log_pred_student = F.log_softmax(logits_student / temperature, dim=1)
    pred_teacher = F.softmax(logits_teacher / temperature, dim=1)
    loss_kd = F.kl_div(log_pred_student, pred_teacher, reduction="none").sum(1).mean()
    loss_kd *= temperature**2
    return loss_kd

import copy
import random
class DoubleKD(Distiller):
    """Distilling the Knowledge in a Neural Network"""

    def __init__(self, student, teacher, cfg):
        super(DoubleKD, self).__init__(student, teacher)
        self.studentB = copy.deepcopy(student)
        self.temperature = cfg.KD.TEMPERATURE
        self.ce_loss_weight = cfg.KD.LOSS.CE_WEIGHT
        self.kd_loss_weight = cfg.KD.LOSS.KD_WEIGHT
        self.logit_stand = cfg.EXPERIMENT.LOGIT_STAND 

    def forward_test(self, image):
        logits_student = self.student(image)[0]
        logits_studentB = self.studentB(image)[0]
        return (logits_student + logits_studentB)/2
    
    def get_learnable_parameters(self):
        # if the method introduces extra parameters, re-impl this function
        v1 = [v for k, v in self.student.named_parameters()]
        v2 = [v for k, v in self.studentB.named_parameters()]
        return v1 + v2

    def forward_train(self, image, target, **kwargs):
        '''sum1 = 0
        sum2 = 0
        for param in self.student.parameters():
            sum1 = sum1 + param.detach().cpu().numpy().sum()
        for param in self.studentB.parameters():
            sum2 = sum2 + param.detach().cpu().numpy().sum()
        with open("/home/banafsh7/projects/def-hadi87/banafsh7/Dist/log.txt", "a") as myfile:
            myfile.write(str(sum1) + "," + str(sum2) + "\n")'''

        if random.random() < 0.5:
            with torch.no_grad():
                logits_student, _ = self.student(image)
            logits_studentB, _ = self.studentB(image)
        else:
            with torch.no_grad():
                logits_studentB, _ = self.studentB(image)
            logits_student, _ = self.student(image)

        logits_student = (logits_student + logits_studentB)/2
        with torch.no_grad():
            logits_teacher, _ = self.teacher(image)

        # losses
        loss_ce = self.ce_loss_weight * F.cross_entropy(logits_student, target)
        loss_kd = self.kd_loss_weight * kd_loss(
            logits_student, logits_teacher, self.temperature, self.logit_stand
        )
        losses_dict = {
            "loss_ce": loss_ce,
            "loss_kd": loss_kd,
        }
        return logits_student, losses_dict
