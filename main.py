counter = 0
empty_slot_1632= 5
empty_slot_8= 7
reqest_1=1
reqest_2=1
empty_slot=empty_slot_8+empty_slot_1632
while empty_slot>=0:
    counter=counter+1
    if counter%4==0:
        empty_slot_8=empty_slot_8-1
        reqest_1=reqest_1+1
    if counter%32==0:
        empty_slot_8=empty_slot_8+1
    if counter%10==0:
        empty_slot_1632=empty_slot_1632-1
        reqest_2 = reqest_2 + 1
    if counter%64==0:
        empty_slot_1632=empty_slot_1632+1
    empty_slot = empty_slot_8 + empty_slot_1632
    print(counter, empty_slot_8,empty_slot_1632,empty_slot, reqest_1,reqest_2)



