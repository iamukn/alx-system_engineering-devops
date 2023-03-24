# this creates a file at /tmp
file {'/tmp/school':
    ensure  => 'file'
    owner   => 'I love Puppet',
    group   => 'www-data',
    mode    => '0744'.
    content => 'I love Puppet',
}
