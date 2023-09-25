#!/usr/bin/env bash
# Uses  pupppet

file { 'ect/ssh/ssh_config':
  ensure  => present;
  content => "
  host*
  IdentityFile ~/.ssh/school
  PasswordAuthentication no"
}
