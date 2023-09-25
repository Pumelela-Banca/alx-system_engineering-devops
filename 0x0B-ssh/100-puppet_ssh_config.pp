#!/usr/bin/env bash
# Uses  pupppet

file { 'ect/ssh/ssh_config':
  ensure  => present;
  content => "Host*  \nIdentityFile ~/.ssh/school\n  PasswordAuthentication no"
}
