**# Feature Flag**

**Implement a JS solution for fetching/reading feature flags from an API. How would you improve** 

   **1.  performance,**

   **2. caching(local storage),**

3. **share across the different app -> we need to use cookies and set the domain properly. Moreover need to create npm package.**

**Use Case: (Config app)**

Depending upon plans, admin/marketing team can turn on / off on the admin dashboard.

example app: **Flagsmith**

```javascript
// src/context/FeatureFlag.js

import React from "react";

export const FeatureFlag = React.createContext({});

export const FeatureFlagProvider = ({children}) => {
	const [feature, setFeatures] = useState({
	  isGooglePayEnabled: true, 
	  isApplePayEnabled: false
        });

	return (
          // for context you need to pass with double braces
	  <FeatureFlag.Provider value={{feature}}>
	    {children}
	  </FeatureFlag.Provider>
}

```


```javascript

import {FeatureFlagProvider} from "./context/FeatureFlag";

const Example = () => {
    return (
	<>
	  <Feature feature="isGooglePayEnabled" value={true}>Google</Feature>
	  <Feature feature="isApplePayEnabled" value={false}>Apple Pay</Feature>
 	</>

}

const Feature = ({feature, children, value}) => {
     const {features} = useContext(FeatureFlag);

    return features[feature] === value ? children : null
}

export default function App() {
	return (
		<FeatureFlagProvider>
		   <Example />
		</FeatureFlagProvide>
	)
}



```
