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
<p><code> 
    
    peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n fabcar --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"changeCarOwner","Args":["CAR9","Dave"]}' 
    
  </code>
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
<p><code> 
  
    peer lifecycle chaincode commit -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt 
    
  </code>

<p> Confirm the chaincode has been committed:
<p><code> peer lifecycle chaincode querycommitted --channelID mychannel --name fabcar --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem </code>

<p> Invoke the chaincode:
<p><code> 
  
    peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n fabcar --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"initLedger","Args":[]}' 
  
  </code>

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
<p>
  <pre>
    <code>

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
  </pre>
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
<p>
  <pre>
   <code> 
   
      class Patient extends Contract {
        async initLedger(ctx) {
            console.info('============= START : Initialize Ledger ===========');
            const patients = [
                {
                    patient_id: '123456',	
                    gender: 'male',
                    address: '1234 Main Street',
                    age: '45',
                    height: '72 in.',
                    weight: '170 lb.',
                    emr: '<path to local directory>',
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

        async createPatient(ctx, patientNumber, patient_id, gender, address, age, height, weight, emr) {
            console.info('============= START : Create Patient ===========');

            const patient = {
                patient_id,					
                docType: 'patient',
                gender,
                address,
                age,
                height,
                weight,
                emr,
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
   
   </code>
  </pre>
<p> Change:
<p><code> module.exports = FabCar; </code>
<p> To:
<p><code> module.exports = Patient; </code>
<p> Navigate to:
<p><code> fabric-samples/fabcar/javascript </code>
<p> Open query.js in text editor
<p> Change evaluateTransactions arguments to:
<p><code> const result = await contract.evaluateTransaction('queryAllPatients'); </code>
<p> Navigate to:
<p><code> fabric-samples/test-network/scripts </code>
<p> Open deployCC.sh in text editor and change chaincodeQuery to:
<p><code> peer chaincode query -C $CHANNEL_NAME -n fabcar -c '{"Args":["queryAllPatients"]}' >&log.txt </code>
<p> Change registerUser.js to make appUser a variable rather than a hard-coded user:
<p>
  <code>
    
    /*
     * SPDX-License-Identifier: Apache-2.0
     */

    'use strict';

    const { Wallets } = require('fabric-network');
    const FabricCAServices = require('fabric-ca-client');
    const fs = require('fs');
    const path = require('path');
    var testUser = "user1234";      // stand-in for website user credentials
    const appUser = testUser; 

    async function main() {
        try {
            // load the network configuration
            const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
            const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

            // Create a new CA client for interacting with the CA.
            const caURL = ccp.certificateAuthorities['ca.org1.example.com'].url;
            const ca = new FabricCAServices(caURL);

            // Create a new file system based wallet for managing identities.
            const walletPath = path.join(process.cwd(), 'wallet');
            const wallet = await Wallets.newFileSystemWallet(walletPath);
            console.log(`Wallet path: ${walletPath}`);

            // Check to see if we've already enrolled the user.
            const userIdentity = await wallet.get('%s', appUser);
            if (userIdentity) {
                console.log('An identity for the user "%s" already exists in the wallet', appUser);
                return;
            }

            // Check to see if we've already enrolled the admin user.
            const adminIdentity = await wallet.get('admin');
            if (!adminIdentity) {
                console.log('An identity for the admin user "admin" does not exist in the wallet');
                console.log('Run the enrollAdmin.js application before retrying');
                return;
            }

            // build a user object for authenticating with the CA
            const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
            const adminUser = await provider.getUserContext(adminIdentity, 'admin');

            // Register the user, enroll the user, and import the new identity into the wallet.
            const secret = await ca.register({
                affiliation: 'org1.department1',
                enrollmentID: '%s', appUser,
                role: 'client'
            }, adminUser);
            const enrollment = await ca.enroll({
                enrollmentID: '%s', appUser,
                enrollmentSecret: secret
            });
            const x509Identity = {
                credentials: {
                    certificate: enrollment.certificate,
                    privateKey: enrollment.key.toBytes(),
                },
                mspId: 'Org1MSP',
                type: 'X.509',
            };
            await wallet.put('appUser', x509Identity);
            console.log('Successfully registered and enrolled admin user "%s" and imported it into the wallet', appUser);

        } catch (error) {
            console.error(`Failed to register user "%s": ${error}`, appUser);
            process.exit(1);
        }
  </code>

<h2> Setting up RESTful API: </h2>
<p>
<p> Navigate to fabcar directory in fabric-samples and start network using javascript:
<code> 
  
    cd fabric-samples/fabcar
    ./startFabric.sh javascript

  </code>
<p> Create apiserver.js
<p> Create a directory for the API and navigate to it:
  <p><code>
    
        mkdir apiserver
        cd apiserver
        
   </code>
<p> Copy apiserver.js and the following files to apiserver directory:
  <p><code>
    
    fabric-samples/fabcar/javascript/package.json
    fabric-samples/fabcar/javascript/wallet/appUser.id
    go/pkg/mod/github.com /hyperledger/fabric-sdk-go@v1.0.0-beta2/pkg/gateway/testdata/connection.json
    
   </code>
<p> Create a directory for wallet inside of apiserver directory:
  <p><code>
    
    cd apiserver
    mkdir wallet
    mv appUser wallet/appUser
    
   </code>
<p> Install required node modules (need to use Node version >10):
  <p><code>
    
    npm install
    npm install express body-parser --save
    
   </code>
<p> Start the server:
  <p><code>
    
    node apiserver.js
    
   </code>
<p> Open a new terminal and check to see if the server is running on port 8080:
  <p><code>
    
    sudo lsof -i -P -n | grep LISTEN
    
   </code>
    
