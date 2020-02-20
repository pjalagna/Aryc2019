file Q1Q2Expansion
queue expansion systems  

overview
- web sites can be overloaded and will stall. the way in which they stall is the same as queues. and queues stall when they become full (volume blocked) or when they become attacked by too many inputs race blocked). web services/sites can be divided into 2 types:
 Q1- those that are entries into the system (front pages/entry) OR internal services 
 Q2 services that output out of the system (EG to the user).


- processes we separate processes by detection of 1 of 2 conditions Volume or Overwhelming traffic (Race)
	-- volume blocking is a condition where the emptying of a queue is not as fast as its input to the point where the maximum number of entries is exceeded. Volume blocking is detected by monitoring the number of entries in the queue.
	Expansion: For services Queues (Q1) the solution is to add more queue bleeding/reading services. to prevent cross execution the recommended process is to route by some separation directive. IE for front pages - splitting off a users input by IP address to a separate clone of the following web service (preferably on a different server). 
	For output queues (type Q2) there can be no expansion of readers. so Volume blockage has to be handled by cloning the output service and redirection by the feeding router to these clones via some seperation directive. 
	
	-- race blocking is a condition where the queue is overwhelmed by input sources. race blocking is detected by heartbeat. heartbeat is the process of trying to push a test message thru the web service and measuring the time that takes to complete (if it completes) or if that time has exceeded a maximum timeout.
	For those websites that face the user (Q1) placing a router in front of the main page could effectively redirect inputs to its own clone pages. the recommended separation directive is to route by time AND by user IP address. the reason for including user IP is to isolate all user traffic into one service track to prevent cross execution. For those internal web services (also considered type Q1) that are race blocked the relieving process the same. installing a (time and IP) router to redirect input to clones of itself.
	For output queues (Q2) - installing a router to redirect input to clones of itself but here time is not a consideration. 
	
	Reduction: once the heartbeat of any primary queue reaches an acceptable minimum then each of its clones are polled for idle. if they (the clones) are idle the feeding router will be adjusted to remove them. and the clone will be instructed to die.
