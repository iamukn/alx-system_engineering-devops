# puppet script to create ssh config file
file_line {
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no'
}

file_line {
    ensure   => 'present',
    path     => '/etc/ssh/ssh_config',
    line     => '    IdentityFile ~/.ssh/school',
}
