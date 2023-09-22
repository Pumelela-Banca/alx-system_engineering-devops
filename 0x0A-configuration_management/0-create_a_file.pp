# Creates file

file { '/tmp/school':
  ensure   => 'file',
  conttent => 'I love Puppet',
  owner    => 'www-data',
  group    => 'www-data',
  mode     => '0744'
}
