import { usePage } from "@inertiajs/react";
import React from "react";

const Chat: React.FC = () => {
  const { props } = usePage<{ post: any }>();
  return <div>Chat do Post: {props.post.title}</div>;
};

export default Chat;
