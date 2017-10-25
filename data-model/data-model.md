# Data Model

[0:00 - 19:00]

## Creating Behavior in a Custom Class

The emerging pattern is that for any behavior that you want to implement, you write the __function__ ('dunder methods' aka data model methods) for the class.

Top level function/Syntax ==> Corresponding __function__
Examples.
    x + y ==> __add__

    init x ==>  __init__

    repr(x) ==>     __repr__

    x() ==>  __call__

The python data model is a means by which you can implement protocols.
Those protocols have some abstract meaning depending on the object itself.

Ex. adding polynomials mens what that means in a math class.
Ex. getting its principle representation means the string input required to create another instance of that object.

In each case:
- this protocol exists
- a dunderscore method implements the protocol
- there is a top level function or syntax that invokes the protocol
    -- usually related to some component

Like many protocols, when we implement something like len, we delegate back to the protocol itself.
- len implemented in terms of len on a constituent object.
- add implemented by adding components (coefficients)
- repr implemented by calling repr on some component

Three core OOP Python patterns to be aware of:
- Protocol View of python
- Built-in Inheritance protocol and how it works
    -- where to look for things on python objects
- Caveats around how Object Orientation works in python

There is a specific feature of python to understand... but lets shelve the protocol oriented data model for now and move on to metaclasses.
