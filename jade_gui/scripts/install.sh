#!/usr/bin/bash
# use bash since we use PIPESTATUS

#TODO: no reflector support
#echo "Running reflector to sort for fastest mirrors" | tee -a /tmp/jade-gui-output.txt
#pkexec reflector --latest 5 --sort rate --save /etc/pacman.d/mirrorlist | tee -a /tmp/jade-gui-output.txt
#TODO: no pkexec
sudo -EH jade config ~/.config/jade.json | tee -a /tmp/jade-gui-output.txt

if [ "${PIPESTATUS[0]}" != "0" ]; then
    cat <<EOF
=============================================
|| Installation Failed  QAQ                ||
=============================================
| Please click 'Next' and try to reboot!    |
|                                           |
| Scroll up to view the installation logs   |
| Logs are also available at the next page  |
|                                           |
| Hope you have better luck next time!      |
+-------------------------------------------+
EOF
    exit 1
fi