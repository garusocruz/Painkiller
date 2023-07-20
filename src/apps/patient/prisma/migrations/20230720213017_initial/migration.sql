-- CreateTable
CREATE TABLE "Patient" (
    "patient_id" TEXT NOT NULL PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER NOT NULL,
    "condition" TEXT NOT NULL
);
