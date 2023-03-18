<?php

# Heredoc
echo <<<KOD
This is a test line that demonstrate 
how to create multiline string in PHP
without using backslash n and ENTER many times.\n
KOD;

# Nowodoc
echo <<<'KOD'
This is a test line that demonstrate 
how to create multiline string in PHP
without using backslash n and ENTER many times.
KOD;
echo "\n";