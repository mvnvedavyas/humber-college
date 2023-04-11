import { getAuth } from "firebase/auth";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { chatRooms } from "../../data/chatRooms";
import { MessageInput } from "../MessageInput";
import { MessageList } from "../MessageList";
import { signOut } from 'firebase/auth';
import { auth } from "../../services/firebase";

function ChatRoom() {
  const params = useParams();
  const [room, setRoom] = useState<any>(chatRooms[0]);

  useEffect(() => {
    const room = chatRooms.find((x) => x.id === params.id);
    if (room) {
      setRoom(room);
    }
  }, [params]);

  const handleSidebarClick = (roomId: string) => {
    setRoom(chatRooms.find((x) => x.id === roomId));
  };

  const logout = () => {
    signOut(auth);
    window.location.reload();
  };

  return (
    <div className="flex flex-row w-screen h-screen">
      {/* Sidebar */}
      <div className="w-1/4 p-4 text-white bg-gray-800">
        <h2 className="mb-4 text-lg font-bold">Chat Rooms</h2>
        <ul>
          {chatRooms.map((room) => (
            <li key={room.id}>
              <div
                onClick={() => handleSidebarClick(room.id)}
                className="block px-4 py-2 rounded hover:bg-gray-700 hover:cursor-pointer"
              >
                {room.title}
              </div>
            </li>
          ))}
          <li key="logout">
            <div
              onClick={logout}
              className="block px-4 py-2 rounded hover:bg-gray-700 hover:cursor-pointer"
            >
              🚪 Logout
            </div>
          </li>
        </ul>
      </div>

      {/* Chat Room */}
      <div className="w-3/4 p-4 bg-gray-900">
        <div className="flex flex-col h-full messages-container">
          <h2 className="py-4 pl-4 mb-2 text-lg font-bold">{room.title}</h2>
          <MessageList roomId={room.id} />
          <MessageInput roomId={room.id} />
        </div>
      </div>
    </div>
  );
}

export { ChatRoom as Landing };
