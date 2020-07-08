EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Lamp circuit"
Date "2019-12-09"
Rev "1"
Comp "Polirecyl"
Comment1 "Basic circuit"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Ngspice:VSOURCE V1
U 1 1 5DEDFB7A
P 3600 4000
F 0 "V1" H 3738 4171 60  0000 L CNN
F 1 "9" H 3738 4097 20  0000 L CNN
F 2 "" H 3600 4100 60  0000 C CNN
F 3 "[[DC]_VALUE]_[AC]_[MAG_[PHASE]]]" H 3600 3820 40  0001 C CNN
	1    3600 4000
	1    0    0    -1  
$EndComp
$Comp
L Ngspice:R R1
U 1 1 5DEDFF3B
P 4350 3400
F 0 "R1" V 4145 3400 50  0000 C CNN
F 1 "900" V 4236 3400 50  0000 C CNN
F 2 "" H 4350 3400 60  0000 C CNN
F 3 "" H 4350 3400 60  0000 C CNN
	1    4350 3400
	0    1    1    0   
$EndComp
$Comp
L Device:LED D1
U 1 1 5DEE07E6
P 4650 3850
F 0 "D1" V 4689 3733 50  0000 R CNN
F 1 "LED" V 4598 3733 50  0000 R CNN
F 2 "" H 4650 3850 50  0001 C CNN
F 3 "~" H 4650 3850 50  0001 C CNN
	1    4650 3850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4650 3400 4650 3700
Wire Wire Line
	4650 4000 4650 4200
Wire Wire Line
	4650 4200 3600 4200
Wire Wire Line
	3600 4200 3600 4000
$Comp
L Switch:SW_SPST SW?
U 1 1 5DEE0C04
P 3850 3400
F 0 "SW?" H 3850 3635 50  0000 C CNN
F 1 "SW_SPST" H 3850 3544 50  0000 C CNN
F 2 "" H 3850 3400 50  0001 C CNN
F 3 "~" H 3850 3400 50  0001 C CNN
	1    3850 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 3400 4150 3400
Wire Wire Line
	4550 3400 4650 3400
Wire Wire Line
	3600 3700 3600 3400
Wire Wire Line
	3600 3400 3650 3400
$EndSCHEMATC
