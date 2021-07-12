from minecraft.networking.packets import Packet
from minecraft.networking.types import ( 
    Byte, Float
)


class PlayerAbilitiesPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x32 if context.protocol_later_eq(550) else \
               0x31 if context.protocol_later_eq(471) else \
               0x2F if context.protocol_later_eq(451) else \
               0x2E if context.protocol_later_eq(389) else \
               0x2D if context.protocol_later_eq(345) else \
               0x2C if context.protocol_later_eq(336) else \
               0x2B if context.protocol_later_eq(332) else \
               0x2C if context.protocol_later_eq(318) else \
               0x2B

    packet_name = 'player abilities'
    definition = [
        {'flags': Byte},
        {'flying_speed': Float},
        {'field_modifier': Float}
    ]
