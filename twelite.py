import binascii
import struct

recvfmt = struct.Struct(">BBBBBIBHBHBBBBBBBBB")
#recvfmt = struct.Struct("<BBBBBIBHBHBBBBBBBBB")

def parse_readdata(line):
    data = recvfmt.unpack(binascii.a2b_hex(line))

    return {
        "sender_id":data[0],
        "command_no":data[1],
        "packet_identity":data[2],
        "protocol_version":data[3],
        "lqi":data[4],
        "sender_number":data[5],
        "receiver_id":data[6],
        "timestamp":data[7],
        "relay_flag":data[8],
        "voltage":data[9],
        "di":[data[11]&0x01, (data[11]&0x02)>>1, (data[11]&0x04)>>2, (data[11]&0x08)>>3],
        "di_change_flag":data[12],
        "ai":[data[13],data[14],data[15],data[16]],
        "ai_efn":data[17],
        "checksum":data[18],
    }
