dangerous_driving = call_model(singletripstream)
if(dangerous_driving==1):
	send_notification(user)
	send_notification(graboperations)