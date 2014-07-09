SplunkHexCommand
================

Encode and decode from and to hex search result data from Splunk

Installation 
================
Install the hexhelper folder as a Splunk command.

Usage examples
================
In the Splunk search bar: 

hexdata | hex decode field1

Will search for "hexdata" and decode the content of field1

hexdata | hex decodeclean field1

Will search for "hexdata" and decode the content of field1 replacing all non ascii characters with a question mark.

asciidata | hex encode field1

Will search for "asciidata" and encode the content of field1 to a hexadecimal representation
