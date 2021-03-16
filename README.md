# CIS433Project

## Start by installing the MetaMask chrome extension which can be found here:
https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en
Follow the installation instructions.

## In order to run this program, navigate to the election directory and input the following commands into your terminal. THE PROGRAM MUST BE RUN ON GOOGLE CHROME.
$ ./setup.sh
## setup.sh runs the following commands:
$ brew install node
$ npm install -g ganache
$ npm install -g truffle
$ npm install -g solc
$ npm install lite-server --save-dev

## Next, open Ganache and select quick start, you should see a list of ETH accounts.

## Then run the following command in the terminal (Making sure you are still in the election directory):
$ ./run_program.sh
## run_program.sh runs the following commands:
$ truffle migrate --reset
$ npm run dev

At this point you should see the sign-in page with several forms, sign in using: [ John, Doe, jdoe@gmail.com, 0, 0, 0 ] or [ Jun, Li, lijun@cs.uoregon.edu, 0, 0, 0 ] where each of these items is placed in their respective field. After successful sign-in, you should see the Oregon State flag, and a loading icon.

## Now sign into MetaMask, the method for sending currency on the blockchain. Some extra steps are going to be completed here since the site is hosted locally.
- Click the MetaMask chrome extension
- Follow the sign-in process, saving your secret key
- Select the networks tab, and select ‘custom RPC’
- Input the following information:
	-- Network Name: election
	-- New RPC URL: http://localhost:7545
	-- Chain ID: 1337
	-- Currency Symbol: ETH

## Navigate to Ganache on your computer
- Click any of the key icons beside the first, and copy the private key
- Next click the circular icon on MetaMask and select Import Account
- Paste the private key string in and press import
- After switching to the account, select the 3 dot menu by the account name, and connect to ‘Election’
- Click the “Not connected” button and select connect on the account
- Now that you are connected refresh the page and the voting menu should appear

## Now you can vote for whichever candidate you would like!
## For pictured instructions please refer to the manual.
