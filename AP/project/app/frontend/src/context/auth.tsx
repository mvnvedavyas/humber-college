import React, { createContext, useState } from 'react';
import { loginWithGoogle } from '../services/firebase';
import { User as FirebaseUser } from "firebase/auth";

export interface AuthContextType {
  user: FirebaseUser | null;
  login: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextType>({
  user: null,
  login: async () => { },
});

const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<any>(null);

  const login = async () => {
    const user = await loginWithGoogle();
    if (!user) {
      window.alert('Error, no login!');
    }

    setUser(user as any);
  };

  const value: AuthContextType = { user, login };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export { AuthProvider };
