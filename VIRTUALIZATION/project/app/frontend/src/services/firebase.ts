import { initializeApp } from "firebase/app";
import {
  GoogleAuthProvider,
  signInWithPopup,
  getAuth,
  User,
} from "firebase/auth";
import {
  getFirestore,
  collection,
  addDoc,
  serverTimestamp,
  onSnapshot,
  query,
  orderBy,
} from "firebase/firestore";

const firebaseConfig = atob(
  "eyJhcGlLZXkiOiJBSXphU3lBT1VfN1FpV2JJWGxJaTM0em5rNGtOUFdqZHRVc05zV0EiLCJhdXRoRG9tYWluIjoic3VyYWotcGVyc29uYWwuZmlyZWJhc2VhcHAuY29tIiwicHJvamVjdElkIjoic3VyYWotcGVyc29uYWwiLCJzdG9yYWdlQnVja2V0Ijoic3VyYWotcGVyc29uYWwuYXBwc3BvdC5jb20iLCJtZXNzYWdpbmdTZW5kZXJJZCI6IjQ4NDQ4NzIxNzExIiwiYXBwSWQiOiIxOjQ4NDQ4NzIxNzExOndlYjo2NGI1NDM3YmU1ZmExZWE5OGQ0N2RhIn0="
);

export const app = initializeApp(JSON.parse(firebaseConfig));
export const auth = getAuth(app);
export const db = getFirestore(app);

/**
 *
 *
 * Helper functions
 *
 **/

async function loginWithGoogle() {
  try {
    const provider = new GoogleAuthProvider();
    const auth = getAuth();

    const { user } = await signInWithPopup(auth, provider);

    return { uid: user.uid, displayName: user.displayName };
  } catch (error) {
    if ((error as any).code !== "auth/cancelled-popup-request") {
      console.error(error);
    }
    return null;
  }
}

async function sendMessage(roomId: string, user: User, text: string) {
  try {
    await addDoc(collection(db, "chat-rooms", roomId, "messages"), {
      uid: user.uid,
      displayName: user.displayName,
      text: text.trim(),
      timestamp: serverTimestamp(),
    });
  } catch (error) {
    console.error(error);
  }
}

function getMessages(roomId: string, callback: any) {
  return onSnapshot(
    query(
      collection(db, "chat-rooms", roomId, "messages"),
      orderBy("timestamp", "asc")
    ),
    (querySnapshot) => {
      const messages = querySnapshot.docs.map((x) => ({
        id: x.id,
        ...x.data(),
      }));

      callback(messages);
    }
  );
}

export { loginWithGoogle, sendMessage, getMessages };
