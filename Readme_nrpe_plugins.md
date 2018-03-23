Checkfile age example
=====================

```
define service {
    host_name               HOSTNAME
    service_description     service_name
    check_command           check_nrpe_linux_file_age!/path/to/dir/!"*.csv"!90000,90000
    notes                   Some useful notes
    notes_url               http://urltodoc/docx
    use                     generic-service
}
```

The files should repect case sensitive on linux.
In the example warning and critical is 25hs = 90000s (when no file found it will reach critical)
