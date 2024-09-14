def cleanup_dict(dictionary):
  cleaned = dict()
  for key, raw_value in dictionary.items():
    cleaned[key] = raw_value.split()
  return cleaned


def nrmp (the_input, quota = 1 ):
  hospital = the_input[0]
  student = the_input[1]
  preference_hospitals = cleanup_dict(the_input[2])
  preference_students = cleanup_dict(the_input[3])

  print(preference_hospitals)
  print(preference_students)

  # while some hospital hi has vacancy and not interviewed all on its preference list,
    # hospital hi offers position to the next student sj
    # if sj is free,
      # sj accepts
    # if not, then sj is already committed to hk
      # if sj prefers hk over hi then,
        # sj remains committed to hk; do nothing
      # else,
        # sj commits to hi
        # increase available slots at hk
        # decrease available slots at hi
  return dict()
