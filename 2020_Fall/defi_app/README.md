# Defi App for Staking

We will create a React app that will stake tokens and offer rewards.

## Goals
1. Build a decentralized application that grants rewards for staking another cryptocurrency.
2. Learn how smart contracts are deployed to the blockchain and how such contracts can be used as code.
3. Bridge the gap between a blockchain "backend" and a React "frontend".
4. Understand how to integrate javascript with smart contracts
5. Connect a Front End with smart contracts

## Requirements
- `Ganache` installed (https://www.trufflesuite.com/ganache)
- `Node.js` installed (https://nodejs.org/)
- `MetaMask` installed on Chrome or Firefox (https://metamask.io/)


## Smart Contracts

1. (Mock) DAI: the DAI token, an ERC20 stable coin, https://www.coindesk.com/price/dai, making it compatible with different ethereum wallets and exchanges.

2. Dapp Token: our made up token. We make our digital bank; people will hold DAI tokens and deposit it into our bank. In return, they'll these Dapp tokens and they can withdraw both.

3. TokenFarm: we will enable "yield farming" to let users earn  interests on new Dapp Tokens, acting as our digital bank.

We will create our Token Farm from scratch, writing out all functions and writing tests against our deployed blockchain.

## About Staking

We will be writing the TokenFarm smart contract, which should take Dai deposits and issue DappTokens.

This will follow 3 primary steps in `2_deploy_contracts.js`:

1. Deploy DAI
2. Deploy DAPP
3. Deploy TokenFarm

We also want to assign all DappTokens to TokenFarm smart contract.

Once the TokenFarm is deployed, we can run the following:
```
mDai = await DaiToken.deployed()      // gets the mockdai smart  contract
accounts=await web3.eth.getAccounts() // gets listof all  accounts on blockchain
accounts[1]                           //  displays the account at  index 1
balance = await mDai.balanceOf(accounts[1]) // sets balance to the balance of account  at  index 1
balance.toString()                    // will show  the   account  balance
web3.utils.fromWei(balance)           //  will reformat the balance to standard that we recognize
```

In order to have our Token Farm do what we want, we need to create functions:

1. Stake tokens, for an investor to deposit their Dai into the Token Farm to begin earning Dapp rewards by staking.
We create mapping in order to update a staking balance and to determine if stakers staked previously. We don't want a staker to appear in our `stakers` list  multiple times. In order to stake tokens, accounts must have a balance greater  than 0.

2. Unstake tokens, for an investor to withdraw from the Dapp. First we  want to get the staking balance and ensure it is over 0 so there is some amount to withdraw. Then we want to drain the entire balance by transferring the balance back to  the dai address. Lastly, we remove this staker from our "pot" of stakers so  they don't earn any more rewards.

3. Issue tokens, which will be called by the owner of a contract. Since the Token Farm has all the Dapp Tokens, we need to create a function to issue rewards to investors. We will issue tokens to all stakers in our `stakers` list. We only want the owner of the contract to be  able to issue tokens, so we restrict the owner  to the  sender.   

Once all this is done in our contracts, we want to create a wrapper for this to easily issue tokens. We create a script that will do just this. Doing the following is the usage for this script:
```
$ truffle exec scripts/issue-token.js
Using network 'development'.

Tokens issued!
$
````


## Tests

We will  use the Chai, a javascript testing library,  https://www.chaijs.com/.

Having .js files in the test library will allow us to run the command `truffle test` to  run the  test  suite.

The before block allows us to create the migration to have the same variables deifned.


## Frontend React App

We will need to start up our npm web server. We will use React for our front end, which means we'll be building out the components. See more at https://reactjs.org/

```
npm run start
```

The first thing  we want to do is turn our web based app into a blockchain application by using the Web3 module, which allows us to establish a connection to Ganache.  We will also use MetaMask and Ganache.

The  `loadWeb3` function will allow us to connect our React app with  our Ganache  blockchain.

In `App.js`, when loading the daiToken, we create a new DaiToken contract and get our balance. We do the same for our DappToken.

We also add a `Main.js` so that it displays all our balances for our corresponding account, including our staked tokens and Dai balance. This will trigger staking a balance specified by the user.

Once there is some amount staked, the owner of the contract can now issue rewards. By opening a terminal, we can run `truffle exec scripts/issue-token.js`. All accounts that have a staking balance will receive an equal amount of DAPP as a reward for staking their tokens.

## Usage:
Upon cloning, from this directory, first run `npm install`.

If you are writing additional smart contracts, you can compile your solidity code with `truffle compile` to ensure it compiles correctly. This creates an `abis` directory, which contains json file that store a description of how the smart contract works.

Then you can run `truffle migrate` to write a transaction to the blockchain. Doing so will require paying for a gas fee. If we look at ourr accounts on Ganache, the first account should've decreased from having 100.00ETH to 99.99ETH.

Once deployed onto the blockchain, we can run `truffle console` to interact with the smart contract. This will open up a truffle console, which is a javascript runtime environment, allowing you to use blockchain, giving us access to any transaction or any smart contract on the blockchain.

For example, once in the environment, you can run:

```
truffle(development)> tokenFarm = await TokenFarm.deployed()
undefined
truffle(development)> tokenFarm
TruffleContract {
  constructor: [Function: TruffleContract] {
    _constructorMethods: {
      configureNetwork: [Function: configureNetwork],
      setProvider: [Function: setProvider],
      ...
      sendTransaction: [Function],
      send: [Function],
      allEvents: [Function],
      getPastEvents: [Function]
    }

truffle(development)> tokenFarm.address
'0xF848A2AE975e9600394DAFA4742F35dD43B32a22'
```

### Running the React App

#### Connecting Ganache and MetaMask
You will need Ganache and MetaMask connected. On MetaMask, add a Custom RPC with:
- Network Name: Ganache
- New RPC URL: http://127.0.0.1:7545
- ChainID: 0x359

#### Connected a Ganache account with MetaMask
Click on the Web3  Circle on the top right to `Import Account` by pasting the private key of one of the Ganache accounts.

Doing this will import the corresponding account so that you can see the  Ganache account's balance in MetaMask.

You should next be ready for the React App.

#### Starting up the Web Server
Run the following in a terminal under the `defi_app` directory. When it executes, open up http://localhost:3000/ and you should see the frontend.

```
npm run start
```

[![Frontend](screenshots/frontend)]

Whenever there is a staking balance, we can issue tokens to reward  those who staked their DAI. In a terminal, running the following will update the rewards balance.
```
$ truffle exec scripts/issue-token.js
Using network 'development'.

Tokens issued!
$
````

[![staked](screenshots/staked)]



### References:
- https://www.youtube.com/watch?v=CgXQC4dbGUE&ab_channel=DappUniversity
- https://github.com/dappuniversity/defi_tutorial
