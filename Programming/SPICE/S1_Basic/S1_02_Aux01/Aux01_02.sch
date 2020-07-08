EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Section 1_2 auxiliary schematics"
Date "2019-12-01"
Rev "1"
Comp "Polirecyl"
Comment1 "Passive components"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R R1
U 1 1 5DE43D70
P 5750 3500
F 0 "R1" V 5543 3500 50  0000 C CNN
F 1 "1k" V 5634 3500 50  0000 C CNN
F 2 "" V 5680 3500 50  0001 C CNN
F 3 "~" H 5750 3500 50  0001 C CNN
	1    5750 3500
	0    -1   1    0   
$EndComp
$Comp
L Device:Battery_Cell V1
U 1 1 5DE43195
P 5250 3900
F 0 "V1" H 5368 3996 50  0000 L CNN
F 1 "1" H 5368 3905 50  0000 L CNN
F 2 "" V 5250 3960 50  0001 C CNN
F 3 "~" V 5250 3960 50  0001 C CNN
	1    5250 3900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5DE44100
P 6250 3850
F 0 "R2" H 6320 3896 50  0000 L CNN
F 1 "2k" H 6320 3805 50  0000 L CNN
F 2 "" V 6180 3850 50  0001 C CNN
F 3 "~" H 6250 3850 50  0001 C CNN
	1    6250 3850
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5900 3500 6250 3500
Wire Wire Line
	6250 3700 6250 3500
Wire Wire Line
	6250 4000 6250 4200
Wire Wire Line
	5250 3700 5250 3500
Wire Wire Line
	5250 3500 5600 3500
Wire Wire Line
	6250 4200 5250 4200
Wire Wire Line
	5250 4200 5250 4000
Text GLabel 6250 3500 0    50   Input ~ 0
NODE2
Text GLabel 5250 3500 0    50   Input ~ 0
NODE1
Text GLabel 5250 4200 0    50   Input ~ 0
0
$EndSCHEMATC
