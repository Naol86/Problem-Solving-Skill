for _ in range(int(input())):
    x = input()
    
    team_a = 0
    team_aq = 0
    
    team_b =0
    team_bq = 0
    for i in range(1, 11):
        if i % 2 != 0:
            if x[i - 1] == '1':
                team_a += 1
            elif x[i - 1] == '?':
                team_aq += 1
        else:
            if x[i - 1] == '1':
                team_b += 1
            elif x[i - 1] == '?':
                team_bq += 1
        if team_a + team_aq + (10 - i)//2 < team_b + team_bq:
            print(i)
            break
        if team_a + team_aq > (team_b + (11 - i)//2):
            print(i)
            # print(team_a, team_b, '-----',(team_b + (11 - i)//2))
            break
        if team_b + team_bq > (team_a + (11 - i)//2):
            print(i)
            break
    else:
        print(10)