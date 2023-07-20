-- CreateTable
CREATE TABLE "Measurement" (
    "measurement_id" TEXT NOT NULL PRIMARY KEY,
    "patient_id" TEXT NOT NULL,
    "blood_pressure" REAL NOT NULL,
    "temperature" TEXT NOT NULL
);
