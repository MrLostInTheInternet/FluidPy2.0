PROGRAM PLC_PRG
VAR
	K0 : BOOL;
	K1 : BOOL;
	K2 : BOOL;
	K3 : BOOL;
	AB0 : BYTE;
	EB0 : BYTE;
	AB1 : BYTE;
	EB1 : BYTE;
END_VAR

//Inputs and Outputs connections
`n//AB* are FLUIDSIM PLC IN, EB* are FLUIDSIM PLC OUT
//A+ -> AB0.1		a1 -> EB0.1
//A- -> AB0.2		a0 -> EB0.2
//B+ -> AB0.3		b1 -> EB0.3
//B- -> AB0.4		b0 -> EB0.4
//C+ -> AB0.5		c1 -> EB0.5
//C- -> AB0.6		c0 -> EB0.6
//D- -> AB0.7		d0 -> EB0.7
//D+ -> AB1.1		d1 -> EB1.1
//E+ -> AB1.2		e1 -> EB1.2
//E- -> AB1.3		e0 -> EB1.3

IF EB0.0 THEN
IF EB0.0 AND EB1.3 AND NOT K0 AND NOT K1 AND NOT K2 AND NOT K3 THEN
	AB0.1 := TRUE;
END_IF;

IF EB0.0 AND NOT K0 AND NOT K1 AND NOT K2 AND NOT K3 THEN
	IF EB0.1 THEN
		K0 := TRUE;
	END_IF;
END_IF;


IF K0 THEN
	AB0.1 := FALSE;
	AB1.3 := FALSE;
END_IF;

IF EB0.1 AND K0 THEN
	AB0.2 := TRUE;
END_IF;

IF EB0.3 AND K1 THEN
	AB0.4 := TRUE;
END_IF;

IF EB0.5 AND K2 THEN
	AB0.6 := TRUE;
END_IF;

IF EB0.7 AND K3 THEN
	AB1.1 := TRUE;
END_IF;


IF K0 THEN
	IF EB0.2 THEN
		AB0.3 := TRUE;
	END_IF;
	IF EB0.3 THEN
		K1 := TRUE;
		K0 := FALSE;
	END_IF;
	IF NOT K0 THEN
		AB0.2 := FALSE;
		AB0.3 := FALSE;
	END_IF;
END_IF;


IF K1 THEN
	IF EB0.4 THEN
		AB0.5 := TRUE;
	END_IF;
	IF EB0.5 THEN
		K2 := TRUE;
		K1 := FALSE;
	END_IF;
	IF NOT K1 THEN
		AB0.4 := FALSE;
		AB0.5 := FALSE;
	END_IF;
END_IF;


IF K2 THEN
	IF EB0.6 THEN
		AB0.7 := TRUE;
	END_IF;
	IF EB0.7 THEN
		K3 := TRUE;
		K2 := FALSE;
	END_IF;
	IF NOT K2 THEN
		AB0.6 := FALSE;
		AB0.7 := FALSE;
	END_IF;
END_IF;


IF K3 THEN
	IF EB1.1 THEN
		AB1.2 := TRUE;
	END_IF;
	IF EB1.2 THEN
		K3 := FALSE;
	END_IF;
	IF NOT K3 THEN
		AB1.1 := FALSE;
		AB1.2 := FALSE;
	END_IF;
END_IF;

IF EB1.2 AND NOT K0 AND NOT K1 AND NOT K2 AND NOT K3 THEN
	AB1.3 := TRUE;
END_IF;
END_IF;