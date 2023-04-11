import { AuthenticatedApp } from "./components/AuthenticatedApp";
import { UnauthenticatedApp } from "./components/UnauthenticatedApp";
import "./App.css";
import { app, auth, db } from "./services/firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import { useCollection } from "react-firebase-hooks/firestore";
import Loading from "./components/Loading";
import { collection, getFirestore } from "firebase/firestore";
import { useEffect, useRef } from "react";

function App() {
  const [user, loading, error] = useAuthState(auth);
  const [value] = useCollection(
    collection(db, "chat-rooms", 'announcements', "messages")
  );
  const previousValueRef = useRef<any>(null);

  useEffect(() => {
    if (previousValueRef.current && value) {
      const newDocuments = value.docs.filter(doc => {
        return !previousValueRef.current.docs.some((prevDoc: { id: string; }) => prevDoc.id === doc.id);
      });
      const newDoc = newDocuments.map(doc => doc.data())
      alert(`New Announcement from ${newDoc[0].displayName}:\n\n ${newDoc[0].text}`)
    }
    previousValueRef.current = value;
  }, [value]);

  if (loading) {
    return <Loading />;
  }

  return (
    <div className="bg-dark-900">
      {user ? <AuthenticatedApp /> : <UnauthenticatedApp />}
    </div>
  );
}

export default App;
