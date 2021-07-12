from minecraft.networking.packets import Packet
from minecraft.networking.types import ( 
    VarInt, Boolean, String, MutableRecord
)


class UpdateLightPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x25 if context.protocol_later_eq(550) else \
               0x24 if context.protocol_later_eq(471) else \
               0x57 if context.protocol_later_eq(461) else \
               0x58 if context.protocol_later_eq(451) else \
               0x57

    packet_name = 'update light'

    definition = [
        {'chunk_x': VarInt},
        {'chunk_y': VarInt},
        {'chunk_z': VarInt},
        {'trust_edges': Boolean},
        {'length_one': VarInt},
        {'sky_light_mask': VarInt},
        {'length_two': VarInt},
        {'block_light_mask': VarInt},
        {'length_there': VarInt},
        {'empty_sky_light_mask': VarInt},
        {'length_four': VarInt},
        {'empty_block_light_mask': Float},
        {'sky_light_array_count': Float},
        {'player_motion_z': Float}
    ]

    position = multi_attribute_alias(Vector, 'x', 'y', 'z')
    # if context.protocol_later_eq(321)
                # and context.protocol_earlier(326)
    player_motion = multi_attribute_alias(
        Vector, 'player_motion_x', 'player_motion_y', 'player_motion_z')
