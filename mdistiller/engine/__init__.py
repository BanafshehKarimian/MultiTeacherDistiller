from .trainer import BaseTrainer, CRDTrainer, AugTrainer, MTSTrainer

trainer_dict = {
    "base": BaseTrainer,
    "crd": CRDTrainer,
    "ours": AugTrainer,
    "MTS": MTSTrainer
}
