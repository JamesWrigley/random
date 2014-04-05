#! /usr/bin/python3

def yak_killer(victim):
    if len(victim) < 3:
        print("String too short!")
        return 0
    else:
#        victim_list = list(victim.replace(" ", ""))
        victim_list = list(victim)
        for i in victim_list:
            if i == "y" and victim_list[victim_list.index(i) + 2] == "k":
                victim_list.__delitem__(victim_list.index(i)+2)
                victim_list.__delitem__(victim_list.index(i)+1)
                victim_list.__delitem__(victim_list.index(i))
    print(''.join(victim_list))

test_str1 = "pakratyakhat"
test_str2 = "quuxyik"
test_str3 = "yukhashbazfooyhkbar"
test_str4 = "C'est grand yak!"

if __name__ == "__main__":
    yak_killer(test_str1)
    yak_killer(test_str2)
    yak_killer(test_str3)
    yak_killer(test_str4)
