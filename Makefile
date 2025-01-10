all:
	echo '#!/bin/bash' > tickets
	echo 'python3 src/tickets.py' >> tickets
	chmod 777 tickets

	echo '#!/bin/bash' > sky_links
	echo 'python3 ./src/sky_links.py' >> sky_links
	chmod 777 sky_links

	echo '#!/bin/bash' > wander
	echo 'python3 src/wander.py' >> wander
	chmod 777 wander

	echo '#!/bin/bash' > communication
	echo 'python3 src/communication.py' >> communication
	chmod 777 communication

	echo '#!/bin/bash' > holidays
	echo 'python3 src/holidays.py' >> holidays
	chmod 777 holidays

	echo '#!/bin/bash' > distribution
	echo 'python3 src/distribution.py' >> distribution
	chmod 777 distribution
