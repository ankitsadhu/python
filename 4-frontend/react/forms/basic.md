[How to create Reusable React Forms? JSON Hooks forms - Part 5 (youtube.com)](https://www.youtube.com/watch?v=rO2U3eFQ440)

multistep form: [Multistep Form Custom Hook With React And TypeScript (youtube.com)](https://www.youtube.com/watch?v=uDCBSnWkuH0)


React Form hook: [React Hook Form Tutorial - 1 - Introduction (youtube.com)](https://www.youtube.com/watch?v=KejZXxFCe2k&list=PLC3y8-rFHvwjmgBr1327BA5bVXoQH-w5s)


Zod

Controlled Form vs uncontrolledfom

uncontrolled form: we dont use react any state management, either we use document.getelementById or useRef

lable htmlfor is bind with id of input

Types of button

1. button
2. submit (default)
3. reset (clear entire form)

onInput vs onChange: only diff same value change is not called in case on onInput


if using files use FormData()

[FormData Demystified: Elevating Form Submissions in Modern Web Applications | by राहुल मिश्रा | Medium](https://rahuulmiishra.medium.com/formdata-demystified-elevating-form-submissions-in-modern-web-applications-ccb325670e90)

e.preventDefault to stop redirection

```js

export const DynamicForm = [{
  type: "text",
  name: "firstName",
  id: "first-name",
  disabled: false,
  error: '',
  value: '',
  validator: function(value) {
   if(value.length < 3) {
     return "Should be greater than 3"
   } else {
     return ""
   }
  }
},{
  type: "textarea",
  name: "address",
  id: "address",
  disabled: false,
  rows: 1,
  error: '',
  value: ''
},{
  type: "password",
  name: "password",
  id: "password ",
  disabled: false,
  error: '',
  value: ''
}]
```


```js



 function App() {
  const [userData, setUserData] = useState(JSON.parse(JSON.stringfy(DynamicForm)))
  
  function handleSubmit(e) {
    e.preventDefault();
    const formData = {}

    userData.forEach(d=> {
     obj[d.name] = d.value;
    })

    console.log(formData)
  
  }
  
  function handleChange({value, name, index}) {
    const oldData = JSON.parse(JSON.stringify(userData));
    oldData[index].value = value;

    if(oldData[index].validator) {
      oldData[index].error = oldData[index].validator(value)
    }
 
    setUserData(oldData)
  }

 return (
  <div>
   <FormWrapper
    inputs={useData}
    onFormSubmit={handleSubmit}
    onFormChange={handleChange}
  </div>
 )
}
```

```js
const FormWrapper = ({
   inputs, 
   onFormSubmit, 
   onFormChange
}) => {
	return (
	 <form onSubmit={onFormSubmit}>
          {inputs.map((data, index) => {
            if(data.type === 'text' || data.type === 'password') {
               return <Textfield 
			{...data} 
			index={index}
			onChange={onFormChange}/>
            } 
   
            if(data.type === "textarea") {
              return <TextArea {...data} index={index}/>
	    }

	    return <TextField {...data} index={index}/>
	  })}
	</form>
	)
}
```

```js

function TextField({
   id = "",
   name = "",
   disabled = false,
   readOnly = false,
   onChange = () => {},
   placeholder = "",
   index = -1, 
   value=""
}) {
  function handleChange(e) {
    onChange({value: e.target.value, name, id, index})
  }

  return {
  <div className={`own-class ${className}`}>
    <input 
	id={id} 
	name={name} 
	disabled={disabled} 
	readOnly={readOnly} 
        placeholder={placeholder}
	type="text" 
        value={value}
	OnInput={onChange}
        className={`own-class ${className}`}} />
	{error && <h2>{error} </h2>}}
  </div>
 }
}


function TextArea({
   id = "",
   name = "",
   disabled = false,
   readOnly = false,
   onChange = () => {},
   placeholder = ""
}) {
  function handleChange(e) {
    onChange({value: e.target.value, name, id})
  }

  return {
  <div>
    <textarea 
	id={id} 
	name={name} 
	disabled={disabled} 
	readOnly={readOnly} 
        placeholder={placeholder} 
	OnInput={onChange}
        rows={rows}
        className={`own-class ${className}`}} />
  </div>
 }
}

```

```js
const [userData, setUserData] = useState({email:"", password: ''})
function handleSubmit(e) {
 e.preventDefault();
 const email = document.getElementById('email').value
 const password = document.getElementById('password').value
}

function handleEmailChange(e) {
  setEmail(e.target.value)
}

function handleChangeFromCustomComp({value, name}) {
  setUserData({...userData, [name]:value})
}

<form onSUbmit={handleSubmit}>
  <div>
   <label htmlFor="email"> user Email </label>
   <input onChange={handleEmailChange} type="email" value={email}/>
  </div>
  
  <TextFiled
    value={userData.email}
    name={'email'} 
    placeholder="" 
    onChange={handleChangeFromCustomComp} />

</form>
```
