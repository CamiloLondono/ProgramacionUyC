-----------ejercicio1

drop TRIGGER if exists ejercicio1;
DELIMITER //
CREATE TRIGGER ejercicio1 AFTER INSERT ON AhorrosParciales
FOR EACH ROW
BEGIN
DECLARE bandera INT;  
SELECT COUNT(*) INTO bandera FROM totalahorro WHERE cliente = NEW.cliente;
IF bandera > 0 THEN
UPDATE totalahorro
SET valor = valor + NEW.valor WHERE cliente = NEW.cliente;
ELSE
INSERT INTO totalahorro (cliente, valor) VALUES (NEW.cliente, NEW.valor);
END IF;
END;
//
DELIMITER ;

------------ ejercicio2

drop TRIGGER if exists ejercicio2;
DELIMITER //
CREATE TRIGGER ejercicio2 AFTER UPDATE ON AhorrosParciales
FOR EACH ROW
BEGIN
DECLARE valor_diferencia FLOAT;
SET valor_diferencia = NEW.valor - OLD.valor;
UPDATE totalahorro
SET valor = valor + valor_diferencia WHERE cliente = NEW.cliente;
END;
//
DELIMITER ;

UPDATE AhorrosParciales SET valor = 100000 WHERE consecutivo = '1' AND cliente = '1115195149';

------------- ejercicio3

drop TRIGGER if exists ejercicio3;
DELIMITER //
CREATE TRIGGER ejercicio3 AFTER UPDATE ON cliente
FOR EACH ROW
BEGIN
IF OLD.nombre <> NEW.nombre THEN
UPDATE cambios
SET nombre = nombre + 1 WHERE cedula = NEW.cedula;
END IF;
IF OLD.apellido <> NEW.apellido THEN
UPDATE cambios
SET apellido = apellido + 1 WHERE cedula = NEW.cedula;
END IF;
IF OLD.telefono <> NEW.telefono THEN
UPDATE cambios
SET telefono = telefono + 1 WHERE cedula = NEW.cedula;
END IF;
END;
//
DELIMITER ;

UPDATE cliente SET nombre = 'Brian' WHERE cedula = '1115030395';

------------ ejercicio4

drop TRIGGER if exists ejercicio4;
DELIMITER //
CREATE TRIGGER ejercicio4 AFTER DELETE ON ahorrosparciales
FOR EACH ROW
BEGIN
UPDATE TotalAhorro
SET valor = valor - OLD.valor WHERE cliente = OLD.cliente;
END;
//
DELIMITER ;

DELETE FROM AhorrosParciales WHERE consecutivo = (SELECT MIN(consecutivo) FROM AhorrosParciales);