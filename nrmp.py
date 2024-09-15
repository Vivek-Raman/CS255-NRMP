def nrmp (the_input, quota = 1):
  if quota <= 0:
    return {}

  preference_of_hospitals = cleanup_dict(the_input[2])
  preference_of_students = cleanup_dict(the_input[3])

  available_slots = quota * len(preference_of_hospitals)
  assigned_hospitals = dict([(key, []) for key in preference_of_hospitals.keys()])
  assigned_students = dict([(key, None) for key in preference_of_students.keys()])

  # while some hospital has vacancy...
  while available_slots > 0:
    # ...and not interviewed all on its preference list...
    hospital = get_hospital_with_free_slot(assigned_hospitals, preference_of_hospitals, quota)
    if hospital is None:
      break

    # hospital offers position to the next preferred student
    preferred_student = preference_of_hospitals[hospital][0]

    # if student is free...
    if (assigned_students[preferred_student] is None):
      # ...student accepts
      my_print(preferred_student + ' accepts ' + hospital)
      assigned_students[preferred_student] = hospital
      assigned_hospitals[hospital].append(preferred_student)
      preference_of_hospitals[hospital] = preference_of_hospitals[hospital][1:]
      available_slots -= 1

    # if not, then student is already committed to another hospital
    else:
      preference_of_student = preference_of_students[preferred_student]
      original_hospital = assigned_students[preferred_student]

      # if student prefers this hospital over their original...
      if preference_of_student.index(hospital) < preference_of_student.index(original_hospital):
        my_print(preferred_student + ' switches from ' + original_hospital + ' to ' + hospital)

        # assign student a slot at new hospital
        assigned_students[preferred_student] = hospital
        assigned_hospitals[hospital].append(preferred_student)

        # release student from original hospital
        assigned_hospitals[original_hospital].remove(preferred_student)

      preference_of_hospitals[hospital] = preference_of_hospitals[hospital][1:]

  # [print(k,v) for k,v in assigned_hospitals.items()]
  return assigned_hospitals


def cleanup_dict(dictionary):
  cleaned = dict()
  for key, raw_value in dictionary.items():
    cleaned[key] = raw_value.split()
  return cleaned


def get_hospital_with_free_slot(assigned_hospitals, preference_of_hospitals, quota):
  for hospital, slots in assigned_hospitals.items():
    if len(slots) < quota and len(preference_of_hospitals[hospital]) > 0:
      return hospital
  return None


should_print = False
def my_print(msg):
  if should_print:
    print(msg)
