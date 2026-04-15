
CREATE OR REPLACE VIEW avg_temp AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;

CREATE OR REPLACE VIEW por_hora AS
SELECT EXTRACT(HOUR FROM timestamp::timestamp) as hora, COUNT(*) as total
FROM temperature_readings
GROUP BY hora;

CREATE OR REPLACE VIEW max_min AS
SELECT DATE(timestamp::timestamp) as data,
MAX(temperature) as max_temp,
MIN(temperature) as min_temp
FROM temperature_readings
GROUP BY data;
