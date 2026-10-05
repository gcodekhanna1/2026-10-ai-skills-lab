#!/bin/zsh
cd -- "${0:A:h}" || exit 1
print "Updating the seating board from the participant lists…"
print ""
converter_python="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
if [[ ! -x "$converter_python" ]]; then
  converter_python="$(command -v python3)"
fi
"$converter_python" make_seating_board.py
board_status=$?
print ""
if [[ $board_status -eq 0 ]]; then
  print "Done! Refresh \"Seating Board.html\" in your browser."
fi
printf "Press Return to close… "
read -r reply
exit "$board_status"
