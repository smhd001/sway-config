#!/bin/bash
echo $@
if [[ -S /tmp/alac.sock ]]
then
  echo socket found
  ~/.cargo/bin/alacritty msg -s /tmp/alac.sock create-window $@
else
  echo not found
  ~/.cargo/bin/alacritty --socket /tmp/alac.sock $@
fi
