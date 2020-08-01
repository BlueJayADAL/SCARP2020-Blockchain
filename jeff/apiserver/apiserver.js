var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');

var app = express();
app.use(bodyParser.json());

// Setting for Hyperledger Fabric
const { Wallets, Gateway } = require('fabric-network');
const path = require('path');
const ccpPath = path.resolve(__dirname, '.',  'connection-org1.json');
//const Wallets = require('/home/etown/scarp/SCARP2020-Blockchain/jeff/fabric-samples/fabcar/javascript/node_modules/fabric-network/lib/impl/wallet/wallets.js');


app.get('/api/queryallpatients', async function (req, res) {
    try {
        // load the network configuration
        //const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        //const walletPath = path.join(process.cwd(), 'wallet');
        //const wallet = await newFileSystemWallet(walletPath);
        //console.log(`Wallet path: ${walletPath}`);


        // Check to see if we've already enrolled the user.
        const identity = await wallet.get('appUser');
        if (!identity) {
            console.log('An identity for the user "appUser" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('fabcar');

        // Evaluate the specified transaction.
        // queryPatient transaction - requires 1 argument, ex: ('queryPatient', 'PAT4')
        // queryAllPatients transaction - requires no arguments, ex: ('queryAllPatients')
        const result = await contract.evaluateTransaction('queryAllPatients');
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);

    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        process.exit(1);
    }
});


app.get('/api/query/:patient_index', async function (req, res) {
    try {
        // load the network configuration
        //const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
        //const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const identity = await wallet.get('appUser');
        if (!identity) {
            console.log('An identity for the user "appUser" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('fabcar');

        // Evaluate the specified transaction.
        // queryPatient transaction - requires 1 argument, ex: ('queryPatient', 'PAT4')
        // queryAllPatients transaction - requires no arguments, ex: ('queryAllPatients')
        const result = await contract.evaluateTransaction('queryPatient', 'PAT0');
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);

    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        process.exit(1);
    }
});

app.post('/api/addpatient/', async function (req, res) {
    try {
        // load the network configuration
        //const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
        //let ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const identity = await wallet.get('appUser');
        if (!identity) {
            console.log('An identity for the user "appUser" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('fabcar');

        // Submit the specified transaction.
        // createPatient transaction - requires 6 argument, ex: ('createPatient', 'PAT12', '5 days', '4 days', '3 days', '2 days')
        await contract.submitTransaction('createPatient', 'PAT1', '10 days', '5 days', '5 days', '2 days');
        console.log('Transaction has been submitted');

        // Disconnect from the gateway.
        await gateway.disconnect();

    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
        process.exit(1);
    }
})

app.listen(8080);