import { useContext } from 'react';
import { AuthContext, AuthContextType } from '../context/auth';

function useAuth(): AuthContextType {
    const value = useContext(AuthContext);
    if (!value) {
        throw new Error("AuthContext's value is undefined.");
    }

    return value;
}

export { useAuth };
