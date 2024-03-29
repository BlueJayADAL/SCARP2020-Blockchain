/*
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const { Contract } = require('fabric-contract-api');

class FabCar extends Contract {

    async initLedger(ctx) {
        console.info('============= START : Initialize Ledger ===========');
        const cars = [
            {
                color: 'blue',
                make: 'Toyota',
                model: 'Prius',
                owner: 'Tomoko',
            },
            {
                color: 'red',
                make: 'Ford',
                model: 'Mustang',
                owner: 'Brad',
            },
            {
                color: 'green',
                make: 'Hyundai',
                model: 'Tucson',
                owner: 'Jin Soo',
            },
            {
                color: 'yellow',
                make: 'Volkswagen',
                model: 'Passat',
                owner: 'Max',
            },
            {
                color: 'black',
                make: 'Tesla',
                model: 'S',
                owner: 'Adriana',
            },
            {
                color: 'purple',
                make: 'Peugeot',
                model: '205',
                owner: 'Michel',
            },
            {
                color: 'white',
                make: 'Chery',
                model: 'S22L',
                owner: 'Aarav',
            },
            {
                color: 'violet',
                make: 'Fiat',
                model: 'Punto',
                owner: 'Pari',
            },
            {
                color: 'indigo',
                make: 'Tata',
                model: 'Nano',
                owner: 'Valeria',
            },
            {
                color: 'brown',
                make: 'Holden',
                model: 'Barina',
                owner: 'Shotaro',
            },
        ];

        for (let i = 0; i < cars.length; i++) {
            cars[i].docType = 'car';
            await ctx.stub.putState('CAR' + i, Buffer.from(JSON.stringify(cars[i])));
            console.info('Added <--> ', cars[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
    }

    async queryCar(ctx, carNumber) {
        const carAsBytes = await ctx.stub.getState(carNumber); // get the car from chaincode state
        if (!carAsBytes || carAsBytes.length === 0) {
            throw new Error(`${carNumber} does not exist`);
        }
        console.log(carAsBytes.toString());
        return carAsBytes.toString();
    }

    async createCar(ctx, carNumber, make, model, color, owner) {
        console.info('============= START : Create Car ===========');

        const car = {
            color,
            docType: 'car',
            make,
            model,
            owner,
        };

        await ctx.stub.putState(carNumber, Buffer.from(JSON.stringify(car)));
        console.info('============= END : Create Car ===========');
    }

    async queryAllCars(ctx) {
        const startKey = 'CAR0';
        const endKey = 'CAR999';
        const allResults = [];
        for await (const {key, value} of ctx.stub.getStateByRange(startKey, endKey)) {
            const strValue = Buffer.from(value).toString('utf8');
            let record;
            try {
                record = JSON.parse(strValue);
            } catch (err) {
                console.log(err);
                record = strValue;
            }
            allResults.push({ Key: key, Record: record });
        }
        console.info(allResults);
        return JSON.stringify(allResults);
    }

    async changeCarOwner(ctx, carNumber, newOwner) {
        console.info('============= START : changeCarOwner ===========');

        const carAsBytes = await ctx.stub.getState(carNumber); // get the car from chaincode state
        if (!carAsBytes || carAsBytes.length === 0) {
            throw new Error(`${carNumber} does not exist`);
        }
        const car = JSON.parse(carAsBytes.toString());
        car.owner = newOwner;

        await ctx.stub.putState(carNumber, Buffer.from(JSON.stringify(car)));
        console.info('============= END : changeCarOwner ===========');
    }

    async changeModel(ctx, carNumber, newModel) {
    	console.info('============= START : changeMake ===========');

    	const carAsBytes = await ctx.stub.getState(carNumber);
    	if (!carAsBytes || carAsBytes.length === 0) {
    	    throw new Error(`${carNumber} does not exist`);
    	}
    	const car = JSON.parse(carAsBytes.toString());
    	car.model = newModel; 

    	await ctx.stub.putState(carNumber, Buffer.from(JSON.stringify(car)));
    	console.info('============= END : changeCarOwner ===========');
    }

}

class Patient extends Contract {

    async initLedger(ctx) {
        console.info('============= START : Initialize Ledger ===========');
        const patients = [
            {
                hospital: '14 days',	// https://clinicaltrials.gov/ct2/show/NCT04372602?cond=COVID-19&draw=2&rank=1
                icu: '7 days',
                ventilator: '8 days',
                vasopressor: '6 days',
            },
    	];

        for (let i = 0; i < patients.length; i++) {
            patients[i].docType = 'patient';
            await ctx.stub.putState('PAT' + i, Buffer.from(JSON.stringify(patients[i])));
            console.info('Added <--> ', patients[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
    }

    async queryPatient(ctx, patientNumber) {
    	const patientAsBytes = await ctx.stub.getState(patientNumber); // get the patient from chaincode state
    	if (!patientAsBytes || patientAsBytes.length === 0) {
    		throw new Error(`${patientNumber} does not exist`);
    	}
    	console.log(patientAsBytes.toString());
    	return patientAsBytes.toString();
    }

    async createPatient(ctx, patientNumber, hospital, icu, ventilator, vasopressor) {
        console.info('============= START : Create Patient ===========');

        const patient = {
            hospital,					// https://clinicaltrials.gov/ct2/show/NCT04372602?cond=COVID-19&draw=2&rank=1
            docType: 'patient',
            icu,
            ventilator,
            vasopressor,
        };

        await ctx.stub.putState(patientNumber, Buffer.from(JSON.stringify(patient)));
        console.info('============= END : Create Patient ===========');
    }

    async queryAllPatients(ctx) {
        const startKey = 'PAT0';
        const endKey = 'PAT999';
        const allResults = [];
        for await (const {key, value} of ctx.stub.getStateByRange(startKey, endKey)) {
            const strValue = Buffer.from(value).toString('utf8');
            let record;
            try {
                record = JSON.parse(strValue);
            } catch (err) {
                console.log(err);
                record = strValue;
            }
            allResults.push({ Key: key, Record: record });
        }
        console.info(allResults);
        return JSON.stringify(allResults);
    }
}

//module.exports = FabCar;
module.exports = Patient; 