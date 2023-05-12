file { '/path/to/directory':
  ensure  => directory,
  mode    => '0755',
  owner   => 'apache',
  group   => 'apache',
  recurse => true,
}
