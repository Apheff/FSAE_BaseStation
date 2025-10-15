import Image from "next/image";


export default function Home() {
  return (
    <div>
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <Image
          className="m-4"
          src="/Logo.svg"
          alt="Unipg Racing Team logo"
          width={140}
          height={32}
          priority
          color=""
        />
      </main>
      <footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
        
          Benvenuto sul sito del Racing Team!
      </footer>
    </div>
  );
}
