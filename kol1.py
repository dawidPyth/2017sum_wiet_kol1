import random

expected_angle = 180


def get_current_angle():
	wing_ground_angle = random.randint(0,360) #shoudl be 0 - 360
	#print wing_ground_angle
	return wing_ground_angle


def correct_to_L_up(current):
	#here current > 180
	corrected_diff = current - expected_angle
	return corrected_diff 

def correct_to_R_up(current):
	#here current < 180
	corrected_diff = expected_angle - current
	return corrected_diff 

while True:
	
	current_angle = get_current_angle()

	print "Current angle: " + str(current_angle)

	if current_angle > 180:
		corrected_left_wing = correct_to_L_up(current_angle)
		print "Left wing should be risen up with " + str(corrected_left_wing) + " units"
	
	if current_angle < 180:
		corrected_right_wing = correct_to_R_up(current_angle)
		print "Right wing should be risen up with " + str(corrected_right_wing) + " units"
	
	


