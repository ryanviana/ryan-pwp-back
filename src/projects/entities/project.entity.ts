import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type ProjectDocument = HydratedDocument<Project>;

@Schema({ timestamps: true })
export class Project {
  @Prop({ required: true })
  title: string;

  @Prop({ required: true })
  description: string;

  @Prop()
  fullDescription: string;

  @Prop({ required: true })
  image: string;

  @Prop({ type: [String], default: [] })
  tags: string[];

  @Prop({ required: true, unique: true })
  slug: string;

  @Prop()
  demoUrl: string;

  @Prop()
  githubUrl: string;

  @Prop({ type: [String], default: [] })
  features: string[];

  @Prop({ default: false })
  featured: boolean;
}

export const ProjectSchema = SchemaFactory.createForClass(Project);
