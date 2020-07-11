<h1> Hyperledger Fabric </h1>

<h2> Prerequisites:</h2>

Add to .bashrc:
<p><code>
export GOPATH=$HOME/go <p>
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
</code>
<p><code>sudo systemctl enable docker</code>
  
Add your user to the docker group:
<p><code>
sudo usermod -a -G docker $USER
</code><p>
Make sure the docker daemon is running:
<p><code> sudo systemctl start docker </code>

<h2> Install samples and binaries: </h2>
<p><code> curl -sSL https://bit.ly/2ysbOFE | bash -s -- 2.0.1 1.4.6 0.4.18 </code>
<p><code> export PATH=<path to download location>/bin:$PATH </code>

<h2> Test network and finish configuration by completing basic tutorials: </h2>
<p><code> cd fabric-samples/test-network </code>
<p> Make sure network is down:
<p><code> ./network.sh down </code>
<p> Bring network up:
<p><code> ./network.sh up </code>
<p> Create channel “mychannel”:
<p><code> ./network.sh createChannel </code>
<p> Start chaincode on channel:
<p><code> ./network.sh deployCC </code>
<p> Add peer binaries to $PATH:
<p><code> export PATH=${PWD}/../bin:${PWD}:$PATH </code>
<p> Add path to fabric-samples and core.yaml:
<p><code> export FABRIC_CFG_PATH=$PWD/../config/ </code>
<p> Add environment variables to Org1:
<p><code> export CORE_PEER_TLS_ENABLED=true </code>
<p><code> export CORE_PEER_LOCALMSPID="Org1MSP" </code>
<p><code> export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt </code>
<p><code> export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp </code>
<p><code> export CORE_PEER_ADDRESS=localhost:7051 </code>
<p> Query car ledger:
<p><code> peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryAllCars"]}' </code>
<p> Change owner of car:
<p><code> peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n fabcar --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"changeCarOwner","Args":["CAR9","Dave"]}' </code>
<p> Add environment variables to Org2:
<p><code> export CORE_PEER_TLS_ENABLED=true </code>
<p><code> export CORE_PEER_LOCALMSPID="Org2MSP" </code>
<p><code> export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt </code>
<p><code> export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp </code>
<p><code> export CORE_PEER_ADDRESS=localhost:9051 </code>
<p> Query Org2 chaincode:
<p><code> peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryCar","CAR9"]}' </code>
<p> Bring the network down:
<code> ./network.sh down </code>
  
<p> Bring up the network with Certificate Authorities:
<p><code> cd fabric-samples/test-network </code>
<p> Make sure network is down:
<p><code> ./network.sh down </code>
<p> Bring up network with CA flag:
<p><code> ./network.sh up -ca </code>
<p> Examine MSP structure:
<p><code> tree organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/ </code>
<p> Bring the network down:
<p><code> ./network.sh down </code>

<p> Deploying a Smart Contract to a channel:
<p><code> cd fabric-samples/test-network </code>
<p><code> ./network.sh down </code>
<p><code> ./network.sh up createChannel </code>

<p> Setup Logspout:
<p> Copy script to current directory:
<p><code> cp ../commercial-paper/organization/digibank/configuration/cli/monitordocker.sh . </code>
<p> Start Logspout:
<p><code> ./monitordocker.sh net_tes t </code>

<p> Package Smart Contract:
<p> Open new terminal window
<p> Install chaincode dependencies:
<p><code> cd fabric-samples/chaincode/fabcar/javascript </code>
<p><code> npm install </code>
<p><code> cd ../../../test-network </code>
<p> Add peer binaries to $PATH </code>
<p><code> export PATH=${PWD}/../bin:${PWD}:$PATH </code>

<p> Add core.yaml to $PATH:
<p><code> export FABRIC_CFG_PATH=$PWD/../config/ </code>

<p> Confirm installed correctly:
<p><code> peer version </code>

<p> Establish Org1 admin as identity:
<p><code> export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp </code>

<p> Create chaincode package:
<p><code> peer lifecycle chaincode package fabcar.tar.gz --path ../chaincode/fabcar/javascript/ --lang node --label fabcar_1 </code>

<p> Install package on peers:

<p> Set environment variables to operate peer CLI as Org1 admin:
<p><code> export CORE_PEER_TLS_ENABLED=true </code>
<p><code> export CORE_PEER_LOCALMSPID="Org1MSP" </code>
<p><code> export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt </code>
<p><code> export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp </code>
<p><code> export CORE_PEER_ADDRESS=localhost:7051 </code>

<p> Install chaincode:
<p><code> peer lifecycle chaincode install fabcar.tar.gz </code>

<p> Same process for Org2:
<p><code> export CORE_PEER_LOCALMSPID="Org2MSP" </code>
<p><code> export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt </code>
<p><code> export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt </code>
<p><code> export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp </code>
<p><code> export CORE_PEER_ADDRESS=localhost:9051 </code>
<p> Approve chaincode definition:
<p><code> peer lifecycle chaincode queryinstalled </code>

<p> Save package id as path variable (replace your package id with the one below):
<p><code> CC_PACKAGE_ID=fabcar_1:69de748301770f6ef64b42aa6bb6cb291df20aa39542c3ef94008615704007f3 </code>

<p> Approve the chaincode:
<p><code> peer lifecycle chaincode approveformyorg -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --package-id $CC_PACKAGE_ID --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem </code>

<p> Set Org1 as admin and approve chaincode definition:
<p><code> export CORE_PEER_LOCALMSPID="Org1MSP" </code>
<p><code> export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp </code>
<p><code> export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt </code>
<p><code> export CORE_PEER_ADDRESS=localhost:7051 </code>
<p><code> peer lifecycle chaincode approveformyorg -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --package-id $CC_PACKAGE_ID --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem </code>

<p> Check if peers have approved chaincode definition:
<p><code> peer lifecycle chaincode checkcommitreadiness --channelID mychannel --name fabcar --version 1.0 --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem --output json </code>

<p> Commit chaincode definition to channel:
<p><code> peer lifecycle chaincode commit -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt </code>

<p> Confirm the chaincode has been committed:
<p><code> peer lifecycle chaincode querycommitted --channelID mychannel --name fabcar --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem </code>

<p> Invoke the chaincode:
<p><code> peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n fabcar --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"initLedger","Args":[]}' </code>

<p> Query the ledger:
<p><code> peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryAllCars"]}' </code>

<p> Clean up the network:
<p><code> docker stop logspout </code>
<p><code> docker rm logspout </code>

<p> Writing an application:

<p> Install build essentials if you haven’t done so:
<p><code> sudo apt install build-essential </code>
<p><code> cd fabric-samples/fabcar </code>
<p><code> ./startFabric.sh javascript </code>
<p><code> cd javascript </code>
<p><code> npm install </code>

<p> Enroll admin user:
<p><code> node enrollAdmin.js </code>

<p> Register and enroll application user:
<p><code> node registerUser.js </code>

<p> Query ledger:
<p><code> node query.js </code>

<p> Change chaincode transaction request:
<p><code> cd fabric-samples/chaincode/fabcar/javascript/lib </code>
<p> Open query.js in text editor
<p> Change line 44 to:
<p><code> const result = await contract.evaluateTransaction('queryCar', 'CAR4'); </code>
<p> Navigate back to fabcar/javascript and run query.js:
<p><code> node query.js </code>

<p> Update the ledger:
<p> Open invoke.js in text editor
<p> Change line 43 to the below and save:
<p><code> await contract.submitTransaction('createCar', 'CAR12', 'Honda', 'Accord', 'Black', 'Tom'); </code>
<p> Run invoke.js:
<p><code> node invoke.js </code>
<p> To see that the transaction has taken place open query.js in text editor and change line 44 to below and save:
<p><code> const result = await contract.evaluateTransaction('queryCar', 'CAR12'); </code>
<p> Run query.js:
<p><code> node query.js </code>
<p> To change a car’s owner, open invoke.js in text editor and change line 43 to below and save:
<p><code> await contract.submitTransaction('changeCarOwner', 'CAR12', 'Dave'); </code>
<p> Run invoke.js:
<p><code> node invoke.js </code>
<p> Query result:
<p><code> node query.js </code>

<p> Shutdown network:
<p><code> cd .. </code>
<p><code> ./networkDown.sh </code>
  
<p> Adding a function to the fabcar chaincode:
<p> Navigate to:
<p><code> fabric-samples/chaincode/fabcar/javascript/lib </code>
<p> Open fabcar.js in text editor
<p> Add following code to Fabcar class:
<p><code>
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
</code>
<p> Navigate to:
<p><code> fabric-samples/fabcar/javascript </code>
<p> Open invoke.js in text editor 
<p> Change arguments of line 43 to:
<p><code> await contract.submitTransaction('changeModel', 'CAR9', 'Civic'); </code>

<h2> Beginning to work with Patient data using the Fabcar sample: </h2>
<p> Navigate to:
<p><code> fabric-samples/chaincode/fabcar/javascript/lib </code>
<p> Open fabcar.js in text editor
<p> Add following class and functions:
<p><code>
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
</code>
<p> Change:
<p><code> module.exports = FabCar; </code>
<p> To:
<p><code> module.exports = Patient; </code>
<p> Navigate to:
<p><code> fabric-samples/fabcar/javascript </code>
<p> Open query.js in text editor
<p> Change evaluateTransactions arguments to:
<p><code> const result = await contract.evaluateTransaction('queryPatient', 'PAT0'); </code>
<p> Navigate to:
<p><code> fabric-samples/test-network/scripts </code>
<p> Open deployCC.sh in text editor and change chaincodeQuery to:
<p><code> peer chaincode query -C $CHANNEL_NAME -n fabcar -c '{"Args":["queryAllPatients"]}' >&log.txt </code>
