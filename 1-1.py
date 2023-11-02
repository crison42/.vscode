def NextDate(Y,M,D):
  # ���������ꡢ�¡����Ƿ�Ϸ�
  if Y <= 0 or M <= 0 or M > 12 or D <= 0:
    return "��Ч����"

  # ����Ƿ�������
  is_leap_year = False
  if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
    is_leap_year = True

  # ����·ݵ������Ƿ�Ϸ�
  if (M == 2 and is_leap_year and D > 29) or (M == 2 and not is_leap_year and D > 28):
    return "��Ч����"
  elif ((M == 4 or M == 6 or M == 9 or M == 11) and D > 30) or (D > 31):
    return "��Ч����"

  # ������һ�������
  if (M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10):
    if D == 31:
      return str(Y) + "-" + str(M+1) + "-1"
    else:
      return str(Y) + "-" + str(M) + "-" + str(D+1)
  elif M == 12:
    if D == 31:
      return str(Y+1) + "-1-1"
    else:
      return str(Y) + "-" + str(M) + "-" + str(D+1)
  elif M == 2:
    if is_leap_year:
      if D == 29:
        return str(Y) + "-3-1"
      else:
        return str(Y) + "-" + str(M) + "-" + str(D+1)
    else:
      if D == 28:
        return str(Y) + "-3-1"
      else:
        return str(Y) + "-" + str(M) + "-" + str(D+1)
  else:
    if D == 30:
      return str(Y) + "-" + str(M+1) + "-1"
    else:
      return str(Y) + "-" + str(M) + "-" + str(D+1)

input = input("���������ڣ���ʽ��yyyy-mm-dd����")
Y,M,D = input.split("-")
Y = int(Y)
M = int(M) 
D = int(D)
NextDate = NextDate(Y,M,D)
print("��һ����"+str(NextDate))