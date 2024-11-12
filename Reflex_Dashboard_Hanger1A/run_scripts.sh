run_scripts.sh
#!/bin/bash

#source ~/dashboard-projects/Reflex_Dashboard_Hanger1A/reflex_env_0.6.2/bin/activate
#(cd ~/dashboard-projects/web_app_entry/backend/ && reflex run --env prod --backend-only) &
#gnome-terminal -- bash -c "cd ~/dashboard-projects/web_app_entry/frontend/ && python -m http.server 3000"
#
#echo "Web app started: Backend in background and Frontend in a new terminal."

#2024_10_22

# Activate virtual environment in the first terminal and start backed
gnome-terminal -- bash -c "
source ~/dashboard-projects/Reflex_Dashboard_Hanger1A/reflex_env_0.6.2/bin/activate;
cd ~/dashboard-projects/web_app_entry/backend/;
reflex run --env prod --backend-only;
exec bash"

# Wait for a few seconds to ensure the backend is up before starting frontend
sleep 5

# Activate virtual environment in the second terminal and start fronend
gnome-terminal -- bash -c "
source ~/dashboard-projects/Reflex_Dashboard_Hanger1A/reflex_env_0.6.2/bin/activate;
cd ~/dashboard-projects/web_app_entry/frontend/;
python -m http.server 3000;
exec bash"

#Launch Chrome with the specified url
google-chrome http://localhost:3000

# Wait for Chrome to close, then terminate backend and fronend
while pgrep -x "chrome" > /dev/null; do
sleep 2
done

# Kill the backend and fronend processes
pkill -f "reflex run --env prod --bakcend-only"
pkill -f "python -m http.server 3000"

echo "Backend and fronend have been terminated."
