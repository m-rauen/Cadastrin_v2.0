from DAOs.dao import DAO 
from entidade.participante import Participante

class ParticipanteDAO(DAO):
    def __init__(self):
        super().__init__('participantes.pkl')
        
    def add(self, participante: Participante):
        if (participante is not None) and isinstance(participante, Participante) and isinstance(participante.codigo, int):
            super().add(participante.codigo, participante)
            
    def update(self, participante:Participante):
        if (participante is not None) and isinstance(participante, Participante) and isinstance(participante.codigo, int):
            super().update(participante.codigo, participante)
            
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
        
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
        
    