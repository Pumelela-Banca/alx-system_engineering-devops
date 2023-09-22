# Creates file

file { 'school':
  ensure   => file,
  path     => '/tmp/school',
  conttent => 'I love Puppet',
  owner    => 'www-data',
  group    => 'www-data',
  mode     => '0744',
}
